from odoo import models, fields, api

from dateutil.relativedelta import *
from datetime import date



class cliente(models.Model):
	_name = 'concesionario.cliente'
	_description = 'model cliente'

	name =fields.Char('NIF',required=True)
	direccion = fields.Char('Direccion',required=True)
	nombre=fields.Char('Nombre',required=True)
	coche_id= fields.Many2one('concesionario.coche',string='Matricula coche')

class coche(models.Model):
	_name = 'concesionario.coche'
	_description = 'model coche'

	name=fields.Char('Id',required=True)
	modelo = fields.Char(string='Modelo',required=True)
	matricula = fields.Char(string='Matricula',required=True)
	fecha= fields.Date(string='Fecha',required=True)
	marca = fields.Char(string='Marca',required=True)


	precio=fields.Integer(string='Precio',required=True)
	cantidad=fields.Integer(string='Cantidad',required=True)
	annos = fields.Integer("Años",compute="_get_annos")
	total= fields.Integer("Total",compute="_get_total")


	cliente_ids = fields.One2many('concesionario.cliente','coche_id',string='Cliente')

	@api.depends('fecha')
	def _get_annos(self):
			for pers in self:
				hoy=date.today()
				pers.annos = relativedelta(hoy,pers.fecha).years

	@api.depends('precio')
	def _get_total(self):
			for pers in self:
				pers.total = pers.precio * pers.cantidad

	


class revision(models.Model):
	_name = 'concesionario.revision'
	_description = 'model revision'

	name = fields.Char('idR',required=True)
	cambioFiltro = fields.Char('Filtro',required=True)
	cambioAceite = fields.Char('Aceite',required=True)
	cambioFrenos = fields.Char('Frenos',required=True)


# class concesionario(models.Model):
#     _name = 'concesionario.concesionario'
#     _description = 'concesionario.concesionario'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
