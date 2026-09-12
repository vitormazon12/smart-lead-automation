CREATE TABLE leads (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    empresa VARCHAR(150),
    interesse VARCHAR(100),
    mensagem TEXT,
    status VARCHAR(30),
    origem VARCHAR(50),
    categoria VARCHAR(50),
    prioridade VARCHAR(20),
    score INTEGER,
    classificacao VARCHAR(30),
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE acoes_lead (
    id SERIAL PRIMARY KEY,
    lead_id INTEGER NOT NULL,
    acao VARCHAR(50) NOT NULL,
    status VARCHAR(30) DEFAULT 'pendente',
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_lead
        FOREIGN KEY (lead_id)
        REFERENCES leads(id)
);

/*--- Consultas úteis 
SELECT * FROM acoes_lead;

SELECT
    id,
    nome,
    email,
    empresa,
    interesse,
    categoria,
    prioridade,
    score,
    classificacao,
    criado_em
FROM leads
ORDER BY id;
---*/