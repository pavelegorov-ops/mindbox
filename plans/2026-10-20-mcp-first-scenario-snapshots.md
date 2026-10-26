# MCP-first snapshots сценариев

Статус: утверждено пользователем 2026-10-20.

## Решение

Live-конфигурация Mindbox, прочитанная через MCP, — источник истины. Локальные
снимки — датированное evidence для ревью; они не доказывают согласование,
сохранение кампании, запуск или фактическую отправку. Active и draft версии
собираются как отдельные версии, а не как «максимальная» версия.

## Scope

1. Добавить отдельный `scenarios/mcp/` контракт и детерминированный рендерер
   raw MCP-ответов: graph, predicates, delays/settings, bindings и зависимости.
2. Не продвигать `latest`, пока комплект `flows_get` + Full для закреплённой
   версии не полон и согласован по `rowVersion`; предыдущий complete сохранить.
3. Сравнивать coherent snapshots по содержанию, включая изменения версий.
4. Перевести текущие инструкции на MCP-first; YAML/DOM-React Flow оставить
   видимым архивным маршрутом, не переписывая legacy-артефакты.
5. Реально read-only проверить репрезентативные пилоты (v3, если они active),
   без изменений объектов Mindbox, commit, push или scheduler.

## Acceptance

- Raw predicates остаются JSON без интерпретации по названию блока.
- Рендер показывает точные campaign GUID/name/channel/mode; email content
  требует отдельный `campaign_get`, а push content остаётся `unknown`, если не
  прочитан.
- Проверены edge targets, reachability, orphan starts, pinned version/
  `rowVersion`, completeness и повторный идемпотентный run.
- Ошибка/неполный вход не меняет `latest` и не затирает complete snapshot.

## Явно вне scope

Массовая выгрузка tenant, scheduler, изменение live-сценариев/кампаний,
перенос или удаление старых YAML/DOM документов, публичные scrapers и другие
типы tenant-данных.