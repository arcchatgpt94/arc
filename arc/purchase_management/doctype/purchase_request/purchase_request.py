import frappe
from frappe.model.document import Document


class PurchaseRequest(Document):
    def validate(self):
        self.calculate_item_amounts()
        self.calculate_total_amount()

    def calculate_item_amounts(self):
        for item in self.items or []:
            qty = frappe.utils.flt(item.qty)
            rate = frappe.utils.flt(item.rate)
            item.amount = qty * rate

    def calculate_total_amount(self):
        self.total_amount = sum(frappe.utils.flt(item.amount) for item in (self.items or []))
