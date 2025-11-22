# RESUMO (Versão Atualizada)

## Projeto: Playlist App

Este documento apresenta:
- Estudo teórico dos padrões de projeto.
- Justificativas detalhadas da aplicação de cada padrão no contexto do projeto.
- Lista dos arquivos reais onde cada padrão está implementado no repositório.
- Entregáveis exigidos.

---

## 1. Estudo Teórico dos Padrões de Projeto

### **Singleton**
Garante que uma classe tenha apenas uma instância e permita acesso global a ela. Usado normalmente para configurações, cache e serviços únicos.

### **Factory Method**
Define uma interface para criar objetos, permitindo que subclasses decidam qual classe instanciar. Reduz acoplamento e facilita extensões.

### **Strategy**
Permite definir uma família de algoritmos, encapsulá-los e torná-los intercambiáveis sem alterar o código cliente.

### **Observer**
Cria um mecanismo de publicação/assinatura para que objetos sejam notificados automaticamente quando um estado muda.

### **Facade**
Fornece uma interface simples para um subsistema complexo.

### **Dependency Injection**
Fornece dependências externas a objetos em vez de deixá-los criá-las internamente, reduzindo acoplamento.

---

## 2. Aplicação dos Padrões no Projeto (Justificativas no Contexto Real)

### **Factory — `factory.py`**
A aplicação possui diferentes formatos/tipos de mídia. O Factory centraliza a criação desses objetos e evita instância direta no código principal.

### **Strategy — `strategies.py`**
As estratégias de reprodução variam (shuffle, ordem, repetição). Cada uma é encapsulada em uma classe separada, facilitando troca dinâmica.

### **Observer — `observers.py`**
O player notifica automaticamente partes interessadas quando ocorrem eventos (mudança de faixa, play/pause). O Observer mantém baixo acoplamento.

### **Facade — `player.py`**
O player integra diversas responsabilidades (carregar faixa, executar, notificar, aplicar estratégias). A classe `Player` atua como fachada para simplificar o uso.

### **Dependency Injection — `main.py` + construtores**
As classes recebem dependências externamente (factory, estratégias, observers). Facilita testes e evolução do projeto.

---

## 3. Onde Encontrar Cada Padrão no Código (Paths Reais do ZIP)

| Padrão | Arquivo(s) | Descrição |
|--------|------------|------------|
| **Factory** | `playlist_app/factory.py` | Criação centralizada de objetos de mídia. |
| **Strategy** | `playlist_app/strategies.py` | Estratégias de reprodução (shuffle, loop etc.). |
| **Observer** | `playlist_app/observers.py` | Sistema de notificação de eventos do player. |
| **Facade** | `playlist_app/player.py` | Interface simplificada do player para o app. |
| **Models** | `playlist_app/models.py` | Estruturas básicas do domínio. |
| **Injeção de Dependências** | `playlist_app/main.py` | Montagem da aplicação e injecção de objetos. |

---

## 4. Entregáveis Exigidos

### **Repositório Git Público contendo:**
- Código-fonte completo.
- Arquivo `RESUMO.md` (este).
- `README.md` com:
  - Descrição completa do projeto.
  - Instruções de instalação/executação.
  - Lista dos padrões implementados e onde encontrá-los.
- Scripts de execução (`run_demo.sh`).

---

## 5. README.md — Conteúdo Recomendado

### **Título:** Playlist App

### **Descrição:**
Aplicação simples para criação, organização e reprodução de playlists com suporte a padrões de projeto.

### **Como executar:**
```bash
sh run_demo.sh
```
OU
```bash
python -m playlist_app.main
```

### **Padrões implementados e locais:**
- Factory → `playlist_app/factory.py`
- Strategy → `playlist_app/strategies.py`
- Observer → `playlist_app/observers.py`
- Facade → `playlist_app/player.py`
- Dependency Injection → `playlist_app/main.py`

---

Se desejar, posso agora gerar automaticamente o README.md final baseado nesta estrutura.
