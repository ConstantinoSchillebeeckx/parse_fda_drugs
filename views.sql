CREATE OR REPLACE VIEW public.products_view AS
 SELECT t1.appl_no,
    t1.product_no,
    t1.form,
    t1.strength,
    t1.reference_drug,
    t1.drug_name,
    t1.active_ingredient,
    t1.reference_standard,
    t3.marketing_status_description,
    t4.appl_type,
    t4.appl_public_notes,
    t4.sponsor_name
   FROM products t1
     LEFT JOIN marketing_status t2 ON t1.appl_no = t2.appl_no AND t1.product_no = t2.Product_no
     LEFT JOIN marketing_status_lookup t3 ON t2.marketing_status_id = t3.marketing_status_id
     LEFT JOIN applications t4 ON t1.appl_no = t4.appl_no;
