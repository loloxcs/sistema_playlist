# Justificativas dos Padrões Utilizados

## Singleton (Player)
- **Por que**: queremos um único player controlando a reprodução na aplicação — estado global do player (fila, índice atual).
- **Problema resolvido**: evita múltiplas instâncias de player que poderiam reproduzir independentemente.
- **Benefícios**: controle centralizado e facilidade de acesso.
- **Sem o padrão**: haveria risco de inconsistência e necessidade de gerenciar instâncias manualmente.

## Factory Method (TrackFactory)
- **Por que**: facilitar a criação de Track a partir de diferentes formatos (dict, CSV).
- **Problema resolvido**: reduz acoplamento do código cliente com formas de construção de objetos.
- **Benefícios**: extensibilidade (adicionar outros métodos de criação).
- **Sem o padrão**: código espalhado com parsing manual em vários pontos.

## Observer (Playlist observers)
- **Por que**: notificar partes interessadas quando a playlist muda (ex.: UI, logger).
- **Problema resolvido**: reduz acoplamento entre playlist e quem reage a mudanças.
- **Benefícios**: flexibilidade; acrescentar novos observadores sem alterar Playlist.
- **Sem o padrão**: playlist teria que chamar diretamente outros módulos ou retornar resultados constantemente.

## Strategy (Playback strategies)
- **Por que**: permitir trocar o comportamento de reprodução (normal, shuffle, reverse) em tempo de execução.
- **Problema resolvido**: evita condicionais complexas no player para diferentes ordens de reprodução.
- **Benefícios**: extensibilidade e código mais limpo.
- **Sem o padrão**: código com muitos if/else dentro do Player.
