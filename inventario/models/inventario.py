# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Producto(models.Model):
    _name = 'inventario.producto'

    codigo = fields.Char(
        max_length=20,
        unique=True
    )
    codigo_barra = fields.Integer(max_length=50)
    descripcion = fields.Char(max_length=200)
    precio = fields.Integer(default=0)
    existencia = fields.Integer(default=0)
    ultima_compra = fields.Date()

    marca_id= fields.Many2one('inventario.marca', string="Marca")
    um_id= fields.Many2one('inventario.um', string="Unidad de Medida")
    subcategoria_id= fields.Many2one('inventario.subcategoria', string="Subcategoria")

    # def __str__(self):
    #     return '{}'.format(self.descripcion) 
    
    # def save(self):
    #     self.descripcion = self.descripcion.upper()
    #     super(Producto, self).save()

    # class Meta:
    #     verbose_name_plural= "Productos"
    #     unique_together = ('codigo', 'codigo_barra') 

class UnidadMedida(models.Model):
    _name = 'inventario.um'
    _rec_name = 'descripcion'
    descripcion = fields.Char(
        max_length=100,
        help_text='Descripción de la Unidad de Medida',
        unique=True
    )

    # def __str__(self):
    #     return '{}'.format(self.descripcion)

    # def save(self):
    #     self.descripcion = self.descripcion.upper()
    #     super(UnidadMedida, self).save()

    # class Meta:
    #     verbose_name_plural= "Unidades de Medida" 

class Marca(models.Model):
    _name= 'inventario.marca'
    _rec_name = 'descripcion'

    descripcion = fields.Char(
        max_length=100,
        help_text='Descripción de la Marca',
        unique=True
    )

    # def __str__(self):
    #     return '{}'.format(self.descripcion)

    # def save(self):
    #     self.descripcion = self.descripcion.upper()
    #     super(Marca, self).save()

    # class Meta:
    #     verbose_name_plural= "Marca" 

class Categoria(models.Model):
    _name='inventario.categoria'
    _rec_name = 'descripcion'

    descripcion = fields.Char(
        max_length=100,
        help_text='Descripción de la Categoría',
        unique=True
    )

    # def __str__(self):
    #     return '{}'.format(self.descripcion)

    # def save(self):
    #     self.descripcion = self.descripcion.upper()
    #     super(Categoria, self).save()

    # class Meta:
    #     verbose_name_plural= "Categorias"

class SubCategoria(models.Model):
    _name = 'inventario.subcategoria'
    _rec_name = 'descripcion'
    
    descripcion = fields.Char(
        max_length=100,
        help_text='Descripción de la Categoría',
    )

    categoria_id = fields.Many2one('inventario.categoria', string="Categoría")


    # def __str__(self):
    #     return'{}:{}'.format(self.categoria.descripcion, self.descripcion)

    # def save(self):
    #     self.descripcion = self.descripcion.upper()
    #     super(SubCategoria, self).save()

    # class Meta:
    #     verbose_name_plural= "SubCategorias"
    #     unique_together = ('categoria', 'descripcion')