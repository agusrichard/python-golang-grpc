CREATE TABLE public.todos (
	id serial NOT NULL,
	title varchar(64) NOT NULL,
	description varchar(256) NULL,
	user_id int4 NULL,
	CONSTRAINT todos_pkey PRIMARY KEY (id)
);