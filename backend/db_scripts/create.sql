CREATE TABLE acesso.empresas (
	id int4 NOT NULL,
	nome varchar(120) NOT NULL,
	cnpj varchar(25) NOT NULL,
	status int4 NOT NULL DEFAULT 1,
	CONSTRAINT empresas_pk PRIMARY KEY (id),
	CONSTRAINT empresas_un UNIQUE (cnpj)
)
WITH (
	OIDS=FALSE
) ;
CREATE INDEX empresas_cnpj_idx ON empresas USING btree (cnpj) ;
CREATE INDEX empresas_id_idx ON empresas USING btree (id) ;
CREATE INDEX empresas_status_idx ON empresas USING btree (status) ;
CREATE TABLE acesso.usuarios (
	id int4 NOT NULL,
	"Identificacao" varchar(35) NOT NULL,
	email varchar(255) NOT NULL,
	password varchar(128) NOT NULL,
	empresa_id int4 NOT NULL,
	data_criacao timestamp NOT NULL,
	status int4 NOT NULL DEFAULT 1,
	CONSTRAINT usuarios_pk PRIMARY KEY (id),
	CONSTRAINT usuarios_un UNIQUE (email, empresa_id),
	CONSTRAINT usuarios_empresas_fk FOREIGN KEY (id) REFERENCES empresas(id)
)
WITH (
	OIDS=FALSE
) ;
CREATE INDEX usuarios_emails_idx ON usuarios USING btree (email) ;
CREATE INDEX usuarios_empresa_id_idx ON usuarios USING btree (empresa_id) ;
CREATE INDEX usuarios_id_idx ON usuarios USING btree (id) ;
CREATE INDEX usuarios_password_idx ON usuarios USING btree (password) ;
CREATE TABLE ged.categorias (
	id int4 NOT NULL,
	empresa_id int4 NOT NULL,
	descricao varchar(128) NOT NULL,
	cor varchar(10) NULL,
	CONSTRAINT categorias_pk PRIMARY KEY (id),
	CONSTRAINT categorias_un UNIQUE (descricao, empresa_id)
)
WITH (
	OIDS=FALSE
) ;
CREATE INDEX categorias_descricao_idx ON ged.categorias USING btree (descricao) ;
CREATE INDEX categorias_empresa_id_idx ON ged.categorias USING btree (empresa_id) ;
CREATE INDEX categorias_id_idx ON ged.categorias USING btree (id) ;
CREATE TABLE ged.arquivos (
	id int4 NOT NULL,
	descricao varchar(128) NOT NULL,
	categoria_id int4 NOT NULL,
	chave varchar(255) NOT NULL,
	usuario_id int4 NOT NULL,
	data_criacao timestamp NOT NULL,
	hash varchar(255) NOT NULL,
	status int4 NOT NULL DEFAULT 1,
	tipo varchar(4) NOT NULL,
	empresa_id int4 NOT NULL,
	CONSTRAINT arquivos_pk PRIMARY KEY (id),
	CONSTRAINT arquivos_un UNIQUE (descricao, tipo, empresa_id),
	CONSTRAINT arquivos_categorias_fk FOREIGN KEY (categoria_id) REFERENCES ged.categorias(id),
	CONSTRAINT arquivos_empresas_fk FOREIGN KEY (empresa_id) REFERENCES empresas(id),
	CONSTRAINT arquivos_usuarios_fk FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
)
WITH (
	OIDS=FALSE
) ;
CREATE INDEX arquivos_categoria_id_idx ON ged.arquivos USING btree (categoria_id) ;
CREATE INDEX arquivos_chave_idx ON ged.arquivos USING btree (chave) ;
CREATE INDEX arquivos_data_criacao_idx ON ged.arquivos USING btree (data_criacao) ;
CREATE INDEX arquivos_descricao_idx ON ged.arquivos USING btree (descricao) ;
CREATE INDEX arquivos_empresa_id_idx ON ged.arquivos USING btree (empresa_id) ;
CREATE INDEX arquivos_hash_idx ON ged.arquivos USING btree (hash) ;
CREATE INDEX arquivos_id_idx ON ged.arquivos USING btree (id) ;
CREATE INDEX arquivos_status_idx ON ged.arquivos USING btree (status) ;
CREATE INDEX arquivos_tipo_idx ON ged.arquivos USING btree (tipo) ;
CREATE INDEX arquivos_usuario_id_idx ON ged.arquivos USING btree (usuario_id) ;

CREATE SEQUENCE acesso.seq_solicitacao
INCREMENT BY 1
MINVALUE 1
MAXVALUE 9223372036854775807
START 1;