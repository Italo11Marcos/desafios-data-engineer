// Cria a tabela anp_sales particionada pela unit
create table anp_sales (
	year_month varchar(7),
	uf varchar(20),
	product varchar(50),
	unit varchar(10),
	volume numeric(10,2),
	created_at timestamp
)
partition by LIST (unit);

CREATE TABLE fuels PARTITION OF anp_sales FOR VALUES IN ('fuels');
CREATE TABLE diesel PARTITION OF anp_sales FOR VALUES IN ('diesel');