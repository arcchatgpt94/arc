import frappe
from frappe.tests.utils import FrappeTestCase


class TestPurchaseRequest(FrappeTestCase):
    def test_amount_is_qty_times_rate(self):
        doc = frappe.get_doc(
            {
                "doctype": "Purchase Request",
                "requester": "Administrator",
                "department": self._ensure_department(),
                "request_date": "2026-05-12",
                "items": [
                    {"doctype": "Purchase Request Item", "item_code": self._ensure_item(), "qty": 3, "rate": 15}
                ],
            }
        )

        doc.insert()

        self.assertEqual(doc.items[0].amount, 45)
        self.assertEqual(doc.total_amount, 45)

    def test_total_amount_sums_all_rows(self):
        item_code = self._ensure_item()
        doc = frappe.get_doc(
            {
                "doctype": "Purchase Request",
                "requester": "Administrator",
                "department": self._ensure_department(),
                "request_date": "2026-05-12",
                "items": [
                    {"doctype": "Purchase Request Item", "item_code": item_code, "qty": 2, "rate": 10},
                    {"doctype": "Purchase Request Item", "item_code": item_code, "qty": 1, "rate": 5},
                ],
            }
        )

        doc.insert()
        self.assertEqual(doc.total_amount, 25)

    def _ensure_item(self):
        item_code = "TEST-ITEM-PR"
        if not frappe.db.exists("Item", item_code):
            frappe.get_doc(
                {
                    "doctype": "Item",
                    "item_code": item_code,
                    "item_name": "Test Item PR",
                    "stock_uom": "Nos",
                    "is_stock_item": 1,
                    "item_group": "All Item Groups",
                }
            ).insert(ignore_permissions=True)
        return item_code

    def _ensure_department(self):
        dept_name = "Test Department PR"
        if not frappe.db.exists("Department", dept_name):
            frappe.get_doc({"doctype": "Department", "department_name": dept_name}).insert(ignore_permissions=True)
        return dept_name
