# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Proveedor(models.Model):

    _name = 'compra.proveedor'

    descripcion=fields.Text(
        max_length=100,
        unique=True
    )
    direccion=fields.Text(
        max_length=250,
        null=True, blank=True
    )
    contacto=fields.Text(
        max_length=100
    )
    telefono=fields.Text(
        max_length=10,
        null=True, blank=True
    )
    email=fields.Text(
        max_length=250,
        null=True, blank=True
    )

class ComprasDet(models.Model):
    _name='compra.detalle'

    producto_id = fields.Many2one('inventario.producto', string='Producto')
    cantidad= fields.Integer(default=0)
    precio_prv=fields.Integer(default=0)
    sub_total=fields.Integer(default=0)
    descuento=fields.Integer(default=0)
    total=fields.Integer(string="Total", compute="_total")
    costo=fields.Float(default=0)

    compra_id= fields.Many2one('compra.compras', string="Compra")
    
    @api.one
    def _total(self):
        self.total = (self.sub_total - self.descuento)

class ComprasEnc(models.Model):
    _name='compra.compras'

    proveedor= fields.Many2one('compra.proveedor', string="Provededor")
    fecha_compra=fields.Date()
    observacion=fields.Text(blank=True, null=True)
    nro_factura=fields.Integer()
    fecha_factura=fields.Date()
    detalle_ids=fields.One2many('compra.detalle','compra_id', string="Detalle de Compra")
    sub_total=fields.Integer()
    descuento=fields.Integer()
    total=fields.Integer()

    