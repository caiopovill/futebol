CREATE DATABASE IF NOT EXISTS pipeline_db;

CREATE TABLE IF NOT EXISTS jogos (
id SERIAL PRIMARY KEY,
home_team VARCHAR(255),
away_team VARCHAR(255),
date VARCHAR(255),
posse_bola_home VARCHAR(255),
posse_bola_away VARCHAR(255),
passes_home VARCHAR(255),
passes_away VARCHAR(255),
passes_corretos_home VARCHAR(255),
passes_corretos_away VARCHAR(255),
total_chutes_home VARCHAR(255),
total_chutes_away VARCHAR(255),
chutes_no_gol_home VARCHAR(255),
chutes_no_gol_away VARCHAR(255),
escanteios_home VARCHAR(255),
escanteios_away VARCHAR(255),
faltas_cometidas_home VARCHAR(255),
faltas_cometidas_away VARCHAR(255),
stage VARCHAR(255),
extraction_date TIMESTAMP NOT NULL
);
