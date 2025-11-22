# Sistema de Playlist de Música (Implementação de Padrões)
Cecilia Rufatto e Lorena Scabello

Projeto de exemplo implementado em Python para a disciplina de Padrões de Projeto.

**Padrões usados**
- Singleton (Player)
- Factory Method (TrackFactory)
- Observer (Playlist observers)
- Strategy (Playback strategies)

## Estrutura
- `playlist_app/` - pacote principal
  - `models.py` - Track, Playlist (Subject)
  - `factory.py` - TrackFactory
  - `player.py` - Player (Singleton)
  - `strategies.py` - Normal, Shuffle, Repeat, Reverse strategies
  - `observers.py` - exemplo de observer (Logger)
  - `main.py` - demo de uso

## Como executar
```bash
python3 -m playlist_app.main
```
Isso executa a demo que mostra criação de playlist, uso da fábrica, observadores e troca de estratégias.
