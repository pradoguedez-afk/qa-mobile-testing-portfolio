# Relatório de Bug — Modelo de Simulação

**ID:** BUG-MOB-001  
**Status:** Simulado / Documentado para Portfólio  
**Severidade:** Média | **Prioridade:** Média  

## Título
[Carrinho] — O contador do carrinho não atualiza imediatamente após clicar em "Add to Cart".

## Passos para reproduzir
1. Abrir o aplicativo My Demo App.
2. Selecionar qualquer produto do catálogo.
3. Tocar no botão "Add to Cart".
4. Observar o ícone do carrinho no canto superior direito.

## Resultado Esperado
O selo/contador do carrinho deve incrementar para `1` imediatamente após a ação.

## Resultado Atual (Simulado)
O contador permanece em `0` até que o usuário navegue para outra tela e retorne ao catálogo.

