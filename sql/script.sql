CREATE TABLE public.users (
	id serial NOT NULL,
	username varchar(128) NULL,
	"password" varchar(256) NULL,
	CONSTRAINT users_pkey PRIMARY KEY (id)
);

CREATE TABLE public.todos (
	id serial NOT NULL,
	title varchar(64) NOT NULL,
	description varchar(256) NULL,
	user_id int4 NULL,
	CONSTRAINT todos_pkey PRIMARY KEY (id)
);