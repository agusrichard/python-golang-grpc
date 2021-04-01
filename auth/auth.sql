CREATE TABLE public.users (
	id serial NOT NULL,
	username varchar(128) NULL,
	"password" varchar(256) NULL,
	CONSTRAINT users_pkey PRIMARY KEY (id)
);