-- pk
ALTER TABLE submission_class_lookup ADD CONSTRAINT submission_class_lookup_pk PRIMARY KEY (submission_class_code_id);
ALTER TABLE applications_docs_type_lookup ADD CONSTRAINT applications_docs_type_lookup_pk PRIMARY KEY (application_docs_type_lookup_id);
ALTER TABLE marketing_status_lookup ADD CONSTRAINT marketing_status_lookup_pk PRIMARY KEY (marketing_status_id);

-- type
ALTER TABLE submissions ALTER COLUMN submission_class_code_id TYPE bigint USING submission_class_code_id::bigint ;

-- fk
ALTER TABLE submissions ADD CONSTRAINT submission_class_lookup_pk FOREIGN KEY (submission_class_code_id) REFERENCES submission_class_lookup(submission_class_code_id);
ALTER TABLE application_docs ADD CONSTRAINT application_docs_id_pk FOREIGN KEY (application_docs_type_id) REFERENCES applications_docs_type_lookup(application_docs_type_lookup_id);
ALTER TABLE marketing_status ADD CONSTRAINT marketing_status_id_pk FOREIGN KEY (marketing_status_id) REFERENCES marketing_status_lookup(marketing_status_id);
