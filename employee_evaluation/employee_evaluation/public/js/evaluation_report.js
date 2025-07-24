frappe.ui.form.on('Evaluation Report', {
    refresh(frm) {
        frm.add_custom_button(__('Print PDF'), () => {
            frappe.call({
                method: 'frappe.utils.print_format.download_pdf',
                args: {
                    doctype: frm.doc.doctype,
                    name: frm.doc.name,
                    format: 'Evaluation Report'
                }
            });
        });
    }
});
