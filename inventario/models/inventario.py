# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Producto(models.Model):
    _name = 'inventario.producto'
    _rec_name = 'nombre'
    codigo = fields.Char(max_length=20, unique=True, string="Código")
    codigo_barra = fields.Integer(max_length=50, unique=True, string="Código de Barra")
    image = fields.Binary()
    nombre = fields.Char(max_length=200, string="Nombre" )
    precio = fields.Integer(default=0)
    existencia = fields.Integer(compute='_calculo_inventario')
    ultima_compra = fields.Date()

    marca_id= fields.Many2one('inventario.marca', string="Marca")
    um_id= fields.Many2one('inventario.um', string="Unidad de Medida")
    subcategoria_id= fields.Many2one('inventario.subcategoria', string="Subcategoria")


    def _calculo_inventario(self):
        compras = self.env['compra.detalle'].search([('producto_id','=',self.id)])
        total_compra = 0
        for compra in compras:
            total_compra += compra.cantidad

        ventas = self.env['venta.detalle_boleta'].search([('producto_id','=',self.id)])
        total_venta = 0
        for venta in ventas:
            total_venta += venta.cantidad
        self.existencia = total_compra - total_venta

class UnidadMedida(models.Model):
    _name = 'inventario.um'
    _rec_name = 'descripcion'
    descripcion = fields.Char(
        max_length=100,
        help_text='Descripción de la Unidad de Medida',
        unique=True
    )


class Marca(models.Model):
    _name= 'inventario.marca'
    _rec_name = 'descripcion'

    descripcion = fields.Char(
        max_length=100,
        help_text='Descripción de la Marca',
        unique=True
    )


class Categoria(models.Model):
    _name='inventario.categoria'
    _rec_name = 'descripcion'

    descripcion = fields.Char(
        max_length=100,
        help_text='Descripción de la Categoría',
        unique=True
    )


class SubCategoria(models.Model):
    _name = 'inventario.subcategoria'
    _rec_name = 'descripcion'
    
    descripcion = fields.Char(
        max_length=100,
        help_text='Descripción de la Categoría',
    )

    categoria_id = fields.Many2one('inventario.categoria', string="Categoría")

