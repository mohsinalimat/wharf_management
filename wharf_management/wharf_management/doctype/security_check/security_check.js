// Copyright (c) 2017, Sione Taumoepeau and contributors
// For license information, please see license.txt

frappe.ui.form.on('Security Check', {

    onload: function(frm) {

//        frappe.call({
//            "method": "frappe.client.get",
//            args: {
//                doctype: "Booking Request",
//                filters: {
//                    'name': frm.doc.booking_ref,
//                    'docstatus': 1,

//                },
//            },
//            callback: function(data) {
//                cur_frm.set_value("current_eta", data.message["eta_date"]);
//                cur_frm.set_value("current_etd", data.message["etd_date"]);
//                cur_frm.set_value("voyage_no", data.message["voyage_no"]);

//                cur_frm.set_value("form_a", data.message["form_a"]);
//                cur_frm.set_value("form_b", data.message["form_b"]);
//                cur_frm.set_value("form_c", data.message["form_c"]);
//                cur_frm.set_value("form_d", data.message["form_d"]);
//                cur_frm.set_value("form_e", data.message["form_e"]);
                //                cur_frm.set_value("agent", data.message["agents"]);
                //                cur_frm.set_value("vessel", data.message["vessel"]);

                //                cur_frm.set_df_property("booking_ref", "read_only", 1);
//                cur_frm.set_df_property("current_eta", "read_only", 1);
//                cur_frm.set_df_property("current_etd", "read_only", 1);
                //                cur_frm.set_df_property("voyage_no", "read_only", 1);
                //                cur_frm.set_df_property("agent", "read_only", 1);
                //                cur_frm.set_df_property("vessel", "read_only", 1);
//            }
//        })

    },

    refresh: function(frm) {

    }
});