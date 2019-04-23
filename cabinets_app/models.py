from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Account(models.Model):
    """ Defines a customer account
    """
    name = models.CharField(max_length=128)
    billing_address = models.CharField(max_length=1024)
    billing_phone = models.CharField(max_length=32)
    billing_email = models.EmailField(max_length=256)
    contact_name = models.CharField(max_length=128)
    discount = models.DecimalField(max_digits=3, decimal_places=2)

    def __repr__(self):
        return f'<Account name: {self.name}>'

    def __str__(self):
        return f'Account name: {self.name}'


class Material(models.Model):
    """ Applied to Project/Cabinet via Specification
    """
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    thickness = models.DecimalField(max_digits=4, decimal_places=2)
    width = models.DecimalField(max_digits=6, decimal_places=2)
    length = models.DecimalField(max_digits=6, decimal_places=2)
    sheet_cost = models.DecimalField(max_digits=6, decimal_places=2)
    waste_factor = models.DecimalField(max_digits=3, decimal_places=2)
    markup = models.DecimalField(max_digits=3, decimal_places=2)
    date_updated = models.DateTimeField(
        default=timezone.now,
        blank=True
    )

    @property
    def sq_ft_cost(self):
        return self.sheet_cost / ((self.width / 12) * (self.length / 12))

    def __repr__(self):
        return f'<Material: {self.name}>'

    def __str__(self):
        return f'{self.name}'


class Hardware(models.Model):
    """ Applied to Project/Cabinet via Specification
    """
    name = models.CharField(max_length=128)
    cost_per = models.DecimalField(max_digits=6, decimal_places=2)
    UNIT_TYPE_CHOICES = [
        ('each', 'Each'),
        ('pair', 'Pair'),
        ('set', 'Set')
    ]
    unit_type = models.CharField(
        choices=UNIT_TYPE_CHOICES,
        max_length=16
    )
    markup = models.DecimalField(max_digits=3, decimal_places=2)

    def __repr__(self):
        return f'<Hardware: {self.name}>'

    def __str__(self):
        return f'{self.name}'


class Labor(models.Model):
    """ Correlates items to labor required, for invoice calculations
    """
    item_name = models.CharField(max_length=128)
    minutes = models.IntegerField()
    units = models.CharField(max_length=32)

    def __repr__(self):
        return f'<Labor: {self.item_name}>'

    def __str__(self):
        return f'{self.item_name}'


class Project(models.Model):
    """ Defines a Project within an Account
    """
    name = models.CharField(max_length=128)
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='projects'
    )
    physical_address = models.CharField(max_length=1024)
    site_contact = models.CharField(max_length=128)
    contact_phone = models.CharField(max_length=32)
    contact_email = models.EmailField(max_length=256)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)

    def __repr__(self):
        return f'<Project name: {self.name}>'

    def __str__(self):
        return f'Project: {self.name}'


class Specification(models.Model):
    """ Defines a default Specification within a Project
    """
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='specifications'
    )
    interior_material = models.ForeignKey(
        Material,
        on_delete=models.SET_NULL,
        null=True,
        related_name='interior_specifications'
    )
    exterior_material = models.ForeignKey(
        Material,
        on_delete=models.SET_NULL,
        null=True,
        related_name='exterior_specifications'
    )
    name = models.CharField(max_length=128)
    CONSTRUCTION_CHOICES = [
        ('frameless', 'Frameless'),
        ('faceframe', 'Faceframe Overlay'),
        ('faceframe-inset', 'Faceframe Inset')
    ]
    construction = models.CharField(
        choices=CONSTRUCTION_CHOICES,
        default='frameless',
        max_length=32
    )
    CATALOG_CHOICES = [
        ('laminate', 'Laminate'),
        ('wood slab', 'Wood Slab'),
        ('wood 5-piece', 'Wood 5-Piece'),
        ('thermofoil', 'Thermofoil')
    ]
    catalog = models.CharField(
        choices=CATALOG_CHOICES,
        default='laminate',
        max_length=32
    )
    FINISH_LEVEL_CHOICES = [
        (0, 'Unfinished'),
        (3, 'Sand & Prep Only'),
        (6, 'Clear'),
        (8, 'Stain'),
        (12, 'Stain & Glaze'),
        (12, 'Stain & Distress'),
        (16, 'Stain, Glaze & Distress'),
        (10, 'Paint'),
        (14, 'Paint & Glaze'),
        (14, 'Paint & Distress'),
        (18, 'Paint, Glaze & Distress')
    ]
    finish_level = models.IntegerField(
        choices=FINISH_LEVEL_CHOICES,
        default=0
    )

    def __repr__(self):
        return f'<Specification name: {self.name}>'

    def __str__(self):
        return f'Project: {self.project.name} | Specification: {self.name}'


class Cabinet(models.Model):
    """ Defines a Cabinet within a Project
    """
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='cabinets'
    )
    specification = models.ForeignKey(
        Specification,
        on_delete=models.CASCADE,
        related_name='cabinets'
    )
    room = models.CharField(max_length=128)
    cabinet_number = models.IntegerField()
    width = models.DecimalField(max_digits=6, decimal_places=2)
    height = models.DecimalField(max_digits=6, decimal_places=2)
    depth = models.DecimalField(max_digits=6, decimal_places=2)
    number_of_doors = models.IntegerField()
    number_of_shelves = models.IntegerField()
    finished_interior = models.BooleanField(default=False)
    finished_left_end = models.BooleanField(default=False)
    finished_right_end = models.BooleanField(default=False)
    finished_top = models.BooleanField(default=False)
    finished_bottom = models.BooleanField(default=False)

    def __repr__(self):
        return f'<Cabinet project: {str(self.project.id)} | Room: {self.room} | Cab No: {self.cabinet_number} >'

    def __str__(self):
        return f'Cabinet for project: {str(self.project.id)} | Room: {self.room} | Cab No: {self.cabinet_number}'


class Drawer(models.Model):
    """ Drawers for Cabinets
    """
    cabinet = models.ForeignKey(
        Cabinet,
        on_delete=models.CASCADE,
        related_name='drawers'
    )
    height = models.DecimalField(max_digits=6, decimal_places=2)
    material = models.ForeignKey(
        Material,
        on_delete=models.SET_NULL,
        null=True,
        related_name='drawer_material'
    )

    def __repr__(self):
        return f'<Drawer for Cab No: {self.cabinet.cabinet_number} in {self.cabinet.project.name}>'

    def __str__(self):
        return f'Drawer for Cab No: {self.cabinet.cabinet_number} in {self.cabinet.project.name}'
