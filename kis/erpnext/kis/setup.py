from __future__ import unicode_literals
import frappe

from frappe import _
from erpnext.setup.utils import insert_record

def setup_healthcare():
	if frappe.db.exists('Medical Department', 'Cardiology'):
		# already setup
		return
	create_medical_departments()

	add_healthcare_service_unit_tree_root()

def create_medical_departments():
	departments = [
		"Accident And Emergency Care" ,"Anaesthetics", "Biochemistry", "Cardiology", "Dermatology",
		"Diagnostic Imaging", "ENT", "Gastroenterology", "General Surgery", "Gynaecology",
		"Haematology", "Maternity", "Microbiology", "Nephrology", "Neurology", "Oncology",
		"Orthopaedics", "Pathology", "Physiotherapy", "Rheumatology", "Serology", "Urology"
	]
	for department in departments:
		medical_department = frappe.new_doc("Medical Department")
		medical_department.department = _(department)
		try:
			medical_department.save()
		except frappe.DuplicateEntryError:
			pass

def get_medical_department(medical_department):

	return medical_department


def add_KIS_service_unit_tree_root():
	record = [
		{
			"doctype": "KIS Service Unit",
			"KIS_service_unit_name": "All KIS Service Units",
			"is_group": 1,
			"company": get_company()
	 	}
	]
	insert_record(record)

def get_company():
	company = frappe.defaults.get_defaults().company
	if company:
		return company
	else:
		company = frappe.get_list("Company", limit=1)
		if company:
			return company[0].name
	return None
