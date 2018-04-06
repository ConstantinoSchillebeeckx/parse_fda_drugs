CREATE OR REPLACE VIEW public.productsview AS
 SELECT t1.index,
    t1."ApplNo",
    t1."ProductNo",
    t1."Form",
    t1."Strength",
    t1."ReferenceDrug",
    t1."DrugName",
    t1."ActiveIngredient",
    t1."ReferenceStandard",
    t3."MarketingStatusDescription",
    t4."ApplType",
    t4."ApplPublicNotes",
    t4."SponsorName"
   FROM "Products" t1
     LEFT JOIN "MarketingStatus" t2 ON t1."ApplNo" = t2."ApplNo" AND t1."ProductNo" = t2."ProductNo"
     LEFT JOIN "MarketingStatus_Lookup" t3 ON t2."MarketingStatusID" = t3."MarketingStatusID"
     LEFT JOIN "Applications" t4 ON t1."ApplNo" = t4."ApplNo";
