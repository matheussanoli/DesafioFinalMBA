# -*- coding: utf-8 -*-
"""Desafio Final

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oaDG-HM306WVi5e5ZMowlEBRjEiXxP8f
"""

!pip install pyspark==3.3.1

import pyspark
from pyspark.sql import SparkSession

spark = (
          SparkSession.builder
                      .master("local[*]")
                      .getOrCreate()
        )

spark

pathTxt = f'/content/drive/MyDrive/Desafio Final Cloud/'
fileTxt = 'MICRODADOS_ENEM_2020.csv'
df = spark.read.format("csv").option("header", "true").option("sep", ";").option("inferSchema", "true").load(f'{pathTxt}{fileTxt}')
df.createOrReplaceTempView("TbEnem")

spark.sql("select *from TbEnem where sg_uf_prova = 'SP' limit 100").show()

#Questão 1 

spark.sql("select count(*) from TbEnem where tp_cor_raca = 0").show()

#Questão 2 

spark.sql("""select count(distinct NU_INSCRICAO) from TbEnem where tp_sexo = 'F' AND sg_uf_ESC = 'SP'""").show()

#Questão 3

spark.sql("""select count(distinct NU_INSCRICAO) from TbEnem where tp_sexo = 'F' AND sg_uf_ESC = 'RS' and Q012 = 'B'""").show()

#Questão 4

spark.sql("""select count(distinct NU_INSCRICAO) AS CONT, sg_uf_ESC from TbEnem GROUP BY sg_uf_ESC ORDER BY 1 DESC """).show()

#Questão 5

spark.sql("""select count(distinct NU_INSCRICAO) AS CONT, sg_uf_ESC from TbEnem where Q002 = "F" GROUP BY sg_uf_ESC ORDER BY 1 asc """).show()

#Questão 6

spark.sql("""select count(distinct NU_INSCRICAO) AS CONT, sg_uf_ESC from TbEnem where TP_FAIXA_ETARIA = 11 GROUP BY sg_uf_ESC ORDER BY 1 desc """).show()

#Questão 7

spark.sql("""select count(distinct NU_INSCRICAO) AS CONT, sg_uf_ESC from TbEnem where Q008 = 'C' GROUP BY sg_uf_ESC ORDER BY 1 desc """).show()

#Questão 8

spark.sql("""select count(distinct NU_INSCRICAO) AS CONT from TbEnem where TP_COR_RACA = 2 and TP_SEXO = "F"  ORDER BY 1 desc """).show()

#Questão 9

spark.sql("""select count(distinct NU_INSCRICAO) AS CONT from TbEnem where TP_NACIONALIDADE = 3  ORDER BY 1 desc """).show()

#Questão 10

dfPublica    = spark.sql("""select avg(NU_NOTA_MT) AS NotaMatematica from TbEnem where TP_ESCOLA = 2""").collect()[0][0]
dfParticular = spark.sql("""select avg(NU_NOTA_MT) AS NotaMatematica from TbEnem where TP_ESCOLA = 3""").collect()[0][0]

print(dfParticular - dfPublica )

#Questão 11

spark.sql("""select count(distinct NU_INSCRICAO) AS CONT, sg_uf_ESC from TbEnem where TP_COR_RACA = 5 and TP_SEXO = "F"  GROUP BY sg_uf_ESC ORDER BY 1 desc """).show()

#Questão 12

dfPai    = spark.sql("""select count(distinct NU_INSCRICAO) AS CONT from TbEnem where Q001 = 'G'""").collect()[0][0]
dfMae    = spark.sql("""select count(distinct NU_INSCRICAO) AS CONT from TbEnem where Q002 = 'G'""").collect()[0][0]

print(dfPai - dfMae )

#Questão 13

spark.sql("""select count(distinct NU_INSCRICAO) AS CONT from TbEnem where Q010 IN ('B','C') and sg_uf_ESC in ('MA','PI','CE','RN','PB','PE','AL','SE','BA')""").collect()[0][0]

#Questão 14

spark.sql("""select count(distinct NU_INSCRICAO) AS CONT from TbEnem where TP_LOCALIZACAO_ESC = 2 and Q025 = 'B'""").collect()[0][0]

#Questão 15

spark.sql("""select count(distinct NU_INSCRICAO),NO_MUNICIPIO_ESC AS CONT from TbEnem GROUP BY NO_MUNICIPIO_ESC ORDER BY 1 DESC""").show()