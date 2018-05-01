from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Payment"),
			"items": [
				{
					"type": "doctype",
					"name": "Wharf Payment Entry",
					"description": _("Wharf Payment Entry"),
				},
				{
					"type": "doctype",
					"name": "Bulk Payment",
					"description": _("Bulk Payment"),
				},
				{
					"type": "doctype",
					"name": "Wharf Payment Fee",
					"description": _("Wharf Payment Fee"),
				},
			]
		},
		{
			"label": _("Cargo Operation"),
			"items": [
				{
					"type": "doctype",
					"name": "Pre Advice",
					"description": _("Pre Advice."),
				},
				{
					"type": "doctype",
					"name": "Cargo",
					"description": _("Cargo."),
				},
				{
					"type": "doctype",
					"name": "Cargo Manifest",
					"description": _("Cargo Manifest."),
				},
				{
					"type": "doctype",
					"name": "Cargo Operation Planning",
					"description": _("Cargo Operation Planning."),
				},

			]
		},
		{
			"label": _("Cargo Movement"),
			"items": [
				{
					"type": "doctype",
					"name": "Transhipment Cargo",
					"description": _("Transhipment Cargo."),
				},
				{
					"type": "doctype",
					"name": "Export",
					"description": _("Export Cargo."),
				},
			]
		},
		{
			"label": _("Warehouse"),
			"items": [
				{
					"type": "doctype",
					"name": "Devaning Request",
					"description": _("Devaning Request."),
				},
				{
					"type": "doctype",
					"name": "Cargo Warehouse",
					"description": _("Warehouse."),
				},
				{
					"type": "doctype",
					"name": "Warehouse Inspection",
					"description": _("Warehouse Inspection."),
				},
				{
					"type": "doctype",
					"name": "Warehouse Custom Check",
					"description": _("Warehouse Custom Check."),
				},
				{
					"type": "doctype",
					"name": "Warehouse Fee Payment",
					"description": _("Warehouse Fee Payment."),
				},
				{
					"type": "doctype",
					"name": "Warehouse Storage Fee",
					"description": _("Warehouse Storage Fee."),
				},
			]
		},
		{
			"label": _("Pilot"),
			"items": [
				{
					"type": "doctype",
					"name": "Pilot Log",
					"description": _("Pilot Log Details."),
				},
			]
		},
		{
			"label": _("Yard Operation"),
			"items": [
				{
					"type": "doctype",
					"name": "Inspection",
					"description": _("Cargo Inspection."),
				},
				{
					"type": "doctype",
					"name": "Yard",
					"description": _("Yard Operation."),
				},
			]
		},
		{
			"label": _("Security"),
			"items": [
				{
					"type": "doctype",
					"name": "Custom Inspection",
					"description": _("Custom Inspection."),
				},
				{
					"type": "doctype",
					"name": "Gate1",
					"description": _("Security Gate 1."),
				},
				{
					"type": "doctype",
					"name": "Bulk Item Count",
					"description": _("Bulk Item Count."),
				},
				{
					"type": "doctype",
					"name": "Gate2",
					"description": _("Security Main Gate."),
				},
				{
					"type": "doctype",
					"name": "Gate1 Export",
					"description": _("Gate1 Export."),
				},
				{
					"type": "doctype",
					"name": "Main Gate Export",
					"description": _("Main Gate Export."),
				},
			]
		},

		{
			"label": _("Fleet Management"),
			"items": [
				{
					"type": "doctype",
					"name": "Vehicle"
				},
				{
					"type": "doctype",
					"name": "Vehicle Log"
				},
			]
		},
		{
			"label": _("Setup"),
			"items": [
				{
					"type": "doctype",
					"name": "Item",
					"description": _("Item."),
				},
				{
					"type": "doctype",
					"name": "Agents",
					"description": _("Agents."),
				},
				{
					"type": "doctype",
					"name": "Vessel Type",
					"description": _("Vessel Type"),
				},
				{
					"type": "doctype",
					"name": "Vessels",
					"description": _("Vessels."),
				},
				{
					"type": "doctype",
					"name": "Cargo Type",
					"description": _("Cargo Type"),
				},
				{
					"type": "doctype",
					"name": "Container Type",
					"description": _("Container Type"),
				},
				{
					"type": "doctype",
					"name": "Ports",
					"description": _("Ports"),
				},
				{
					"type": "doctype",
					"name": "Shift",
					"description": _("Working Shift"),
				},
				{
					"type": "doctype",
					"name": "Work Type",
					"description": _("Work Type"),
				},
				{
					"type": "doctype",
					"name": "Container Truck",
					"description": _("Container Truck"),
				},
				{
					"type": "doctype",
					"name": "Truck Drivers",
					"description": _("Truck Drivers"),
				},
			]
		},
		{
			"label": _("Fees"),
			"items": [
				
				{
					"type": "doctype",
					"name": "Wharf Handling Fee",
					"description": _("Wharf Handling Fee"),
				},
				{
					"type": "doctype",
					"name": "Berthage Fee",
					"description": _("Berthage Fee"),
				},
				{
					"type": "doctype",
					"name": "Storage Fee",
					"description": _("Storage Fee"),
				},
			
				{
					"type": "doctype",
					"name": "Wharfage Fee",
					"description": _("Wharfage Fee"),
				},
				{
					"type": "doctype",
					"name": "Devanning Fee",
					"description": _("Devanning Fee"),
				},
			]
		},
		{
			"label": _("Reports"),
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Cargo Movement",
					"doctype": "Cargo Movement"
				},
			]
		},
		{
			"label": _("Reports"),
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Cargo Statitics",
					"doctype": "Cargo Statitics"
				},
			]
		},
		{
			"label": _("Reports"),
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Cargo Report",
					"doctype": "Cargo Report"
				},
			]
		},
		{
			"label": _("Reports"),
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Vessels Report",
					"doctype": "Vessels Report"
				},
			]
		},
	]
