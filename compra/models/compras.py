# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Compra(models.Model):
    _name='compra.compras'
    _rec_name= 'nro_factura'
    fecha_compra=fields.Date( string = u'Fecha de emisión', default = fields.Date.context_today)
    observacion=fields.Text(blank=True, null=True)
    nro_factura=fields.Char(max_length=100)
    proveedor_id=fields.Many2one('compra.proveedor', string = " Proveedor")
    detalle_ids=fields.One2many('compra.detalle','compras_id', string = "Detalle de la compra")
    sub_total=fields.Integer(compute="_sub_total")
    descuento=fields.Integer(default=0)
    total=fields.Integer(string= 'Total compra', compute= '_total_compras')
    @api.one
    @api.depends('detalle_ids')
    def _sub_total(self):
        for detalle in self.detalle_ids:
            self.sub_total+=detalle.total

    @api.one
    def _total_compras(self):
        self.total = (self.sub_total - ((self.descuento)/100)* self.sub_total)
        return self.total

class DetalleCompra(models.Model):
    _name='compra.detalle'
    _rec_name = 'total'
    producto=fields.Many2one('inventario.producto', string = "Producto")
    cantidad= fields.Integer()
    precio_unitario=fields.Integer()
    sub_total=fields.Integer(string= 'Sub total', compute= '_sub_total')
    descuento=fields.Integer(default=0)
    total=fields.Integer(string= 'Total precio de producto', compute= '_total_detalle')
    compras_id=fields.Many2one('compra.compras', string = "Nro de Factura")
    @api.one
    def _sub_total(self):
        self.sub_total = (self.cantidad * self.precio_unitario)

    @api.one
    def _total_detalle(self):
        self.total = (self.sub_total - ((self.descuento)/100)* self.sub_total)

class Proveedor(models.Model):
    _name = 'compra.proveedor'
    _rec_name='nombre'
    nombre=fields.Text(blank=True, null=True)
    direccion=fields.Text(blank=True, null=True)
    contacto=fields.Text(blank=True, null=True)
    telefono= fields.Integer(default=0)
    email=fields.Text(blank=True, null=True)