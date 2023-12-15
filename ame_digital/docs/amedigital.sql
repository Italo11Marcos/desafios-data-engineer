/*Qual a quantidade de respondentes de cada país?*/
select
p.nome as pais,
count(p.nome) as quantidade 
from respondente r
inner join paises p on r.pais_id = p.id
group by p.nome
order by 2 desc

/*Quantos usuários que moram em United States gostam de Windows?*/
select
count(r.id) as total
from respondente r
inner join sistemas_operacionais so on r.sistema_operacional_id = so.id
inner join paises p on r.pais_id = p.id
where p.nome = 'United States' and so.nome = 'Windows'

/*Qual a média de salário dos usuários que moram em Israel e gostam de Linux?*/
select
round(avg(r.salario)::numeric, 2) as media_salarial
from respondente r
inner join sistemas_operacionais so on r.sistema_operacional_id = so.id
inner join paises p on r.pais_id = p.id
where p.nome = 'Israel' and so.nome like 'Linux%'

/*Qual a média e o desvio padrão do salário dos usuários que usam Slack para cada tamanho de empresa disponível?*/ 
with resp_slack as (
	select
	ruf.respondente_id
	from resp_usa_ferramenta ruf
	inner join ferramentas_comunicacao fc on ruf.ferramenta_comunic_id = fc.id
	where fc.nome = 'Slack'
	group by 1
)
select
e.tamanho,
round(avg(r.salario)::numeric, 2) as media_salarial,
round(stddev(r.salario)::numeric, 2) as desvio_p_salario
from respondente r 
inner join resp_slack rs on r.id = rs.respondente_id
inner join empresas e on r.empresa_id = e.id
group by 1

/* Qual a diferença entre a média de salário dos respondentes 
do Brasil que acham que criar código é um hobby e a média de todos de 
salário de todos os respondentes brasileiros agrupado por cada sistema operacional que eles usam? */
with salario_hobby as (
	select
	round(avg(r.salario)::numeric, 2) as media_hobby,
	so.nome
	from respondente r
	inner join sistemas_operacionais so on r.sistema_operacional_id = so.id
	inner join paises p on r.pais_id = p.id
	where r.programa_hobby = 1 and p.nome = 'Brazil'
	group by so.nome
), salario_geral as (
	select
	round(avg(r.salario)::numeric, 2) as media_geral,
	so.nome
	from respondente r
	inner join sistemas_operacionais so on r.sistema_operacional_id = so.id
	inner join paises p on r.pais_id = p.id
	where p.nome = 'Brazil'
	group by so.nome
)
select
sh.nome as sistema_operacional,
media_hobby,
media_geral,
media_hobby - media_geral as media_diff
from salario_hobby sh
inner join salario_geral sg on sh.nome = sg.nome

/*Quais são as top 3 tecnologias mais usadas pelos desenvolvedores?*/
select
lp.nome,
count(lp.nome)
from linguagens_programacao lp
inner join resp_usa_linguagem rul on rul.linguagem_programacao_id = lp.id
group by 1
order by 2 desc
limit 3

/*Quais são os top 5 países em questão de salário?*/
select
round(avg(r.salario)::numeric, 2) as media_salarial,
p.nome
from respondente r 
inner join paises p on r.pais_id = p.id
group by 2
order by 1 desc
limit 5

/*Quantos usuários ganham mais de 5 salários mínimos em cada um desses países.
 * United States = 4.787,90
 * India = 243,52
 * United Kingdom = 6.925,63
 * Germany = 6.664,00
 * Canada = 5.567,68
 */
select
count(m.qnt_salario_min) as qnt_min,
m.pais
from(
	select
	case
		when s.pais = 'United States' then floor(s.salario / 4787.90)
		when s.pais = 'Germany' then floor(s.salario / 6664)
		when s.pais = 'India' then floor(s.salario / 243.52)
		when s.pais = 'Canada' then floor(s.salario / 5567.68)
		when s.pais = 'United Kingdom' then floor(s.salario / 6925.63)
	end qnt_salario_min,
	s.pais
	from (
		select
		r.id,
		r.salario,
		p.nome as pais
		from respondente r 
		inner join paises p on r.pais_id = p.id
		where p.nome in ('United States', 'India', 'United Kingdom', 'Germany', 'Canada')
	) s
) m
where m.qnt_salario_min > 4
group by 2
order by 1 desc