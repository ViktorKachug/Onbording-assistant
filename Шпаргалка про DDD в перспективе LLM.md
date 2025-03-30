# Шпаргалка про DDD в перспективе LLM

## Пропускаем эти термины

Это тактические термины. Они полезны при разработке систем, но не обязательно применимы к LLM. Смело их пропускаем:

**Aggregate Root** — **Корневой агрегат** ([practicalDDD/docs/aggregate.md at master · MaksimDzhangirov/practicalDDD · GitHub](https://github.com/MaksimDzhangirov/practicalDDD/blob/master/docs/aggregate.md#:~:text=%D0%9A%D0%BE%D1%80%D0%BD%D0%B5%D0%B2%D0%BE%D0%B9%20%D0%B0%D0%B3%D1%80%D0%B5%D0%B3%D0%B0%D1%82%20%28,Aggregate%20Root))  
The primary entity in an _Aggregate_ (a cluster of related objects treated as one unit) that acts as the gatekeeper. All external references go through the aggregate root, which ensures the integrity and consistency of the aggregate’s invariants.

**Entity** — **Сущность** ([Domain-Driven Design: тактическое проектирование. Часть 2 / Хабр](https://habr.com/ru/articles/316890/#:~:text=%D0%A1%D1%83%D1%89%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20))  
An object defined by its identity rather than its attributes. An entity has a unique identifier and persists through state changes over time (e.g. a Customer with an ID remains the same customer even if their data changes)​.

**Value Object** — **Объект-значение** ([Domain-Driven Design: тактическое проектирование. Часть 2 / Хабр](https://habr.com/ru/articles/316890/#:~:text=%D0%9E%D0%B1%D1%8A%D0%B5%D0%BA%D1%82)) An immutable object that has _no unique identity_; it is defined only by the values of its attributes. Two value objects with the same attribute values are considered equal, and any change to a value object is done by replacing it with a new instance​.

**Repository** — **Репозиторий** ([Агрегаты в Domain-Driven-Design и C# | OTUS](https://otus.ru/nest/post/1187/#:~:text=%D0%A0%D0%B5%D0%BF%D0%BE%D0%B7%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D0%B9%20%E2%80%94%20%D1%8D%D1%82%D0%BE%20%D0%BE%D1%87%D0%B5%D0%BD%D1%8C%20%D0%BF%D0%BE%D0%BF%D1%83%D0%BB%D1%8F%D1%80%D0%BD%D1%8B%D0%B9,%D0%B8%D0%B7%20%D0%B1%D0%B0%D0%B7%D1%8B%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85%20%D0%B0%D0%B3%D1%80%D0%B5%D0%B3%D0%B0%D1%82%20%D0%B8)) An abstraction for data access that mediates between the domain and the data source. It provides operations to retrieve, add, and persist domain objects from a underlying store (e.g., database) while shielding the domain from database details​

**Domain Event** — **Событие предметной области** ([Domain-Driven Design: тактическое проектирование. Часть 2 / Хабр](https://habr.com/ru/articles/316890/#:~:text=%D0%A1%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B5%20)) A representation of a significant occurrence in the domain, expressed in the ubiquitous language. For example, _“Order Shipped”_ or _“Delivery Cancelled”_ are domain events. Such an event is used to notify other parts of the system that something important has happened in the domain​.

**Factory** — **Фабрика** ([Domain-Driven Design: тактическое проектирование. Часть 2 / Хабр](https://habr.com/ru/articles/316890/#:~:text=%D0%A4%D0%B0%D0%B1%D1%80%D0%B8%D0%BA%D0%B0%20)) A construct (often a method or object) that handles the _creation of domain objects_. Factories encapsulate complex instantiation logic, ensuring that aggregates or entities are created in a consistent state and relieving other parts of the code from knowing how to construct those objects​

**Specification** — **Спецификация** ([Спецификация (шаблон проектирования) — Википедия](https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B5%D1%86%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D1%8F_\(%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD_%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F\)#:~:text=%C2%AB%D0%A1%D0%BF%D0%B5%D1%86%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D1%8F%C2%BB%20%D0%B2%20%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B8%20%C2%A0%E2%80%94%20%D1%8D%D1%82%D0%BE,%D0%BC%D0%BE%D0%B6%D0%B5%D1%82%20%D0%B1%D1%8B%D1%82%D1%8C%20%D0%BF%D1%80%D0%B5%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%BE%20%D0%B2%20%D0%B2%D0%B8%D0%B4%D0%B5)) A design pattern that encapsulates a business rule or criteria as an object, which can evaluate to true/false for a given candidate object.

## Обращаем внимание на эти термины

А вот на эти термины стоит обращать внимание при чтении книг и статей. Связанные с ними концепции сильно меня выручают при переносе сложных процессов на LLM.

**Ubiquitous Language** — **Единый язык** ([Domain-Driven Design: стратегическое проектирование. Часть 1 / Habr](https://habrahabr.ru/post/316438/#:~:text=%D0%95%D0%B4%D0%B8%D0%BD%D1%8B%D0%B9%20%D1%8F%D0%B7%D1%8B%D0%BA))  
A shared, rigorous vocabulary developed by the team (developers _and_ domain experts) to describe the domain. This common language is based on the domain model and is used consistently in conversations, documentation, and code to avoid ambiguity.

**Bounded Context** — **Ограниченный контекст** ([Domain-Driven Design: стратегическое проектирование. Часть 1 / Habr](https://habrahabr.ru/post/316438/#:~:text=%D0%9E%D0%B3%D1%80%D0%B0%D0%BD%D0%B8%D1%87%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BA%D1%81%D1%82))  
A logical boundary within which a particular domain model is defined and applicable. Inside a bounded context, terms in the ubiquitous language have a specific meaning and the model remains consistent. It ensures clarity and separation of concerns, since the same terms might mean something different in another context​

**Domain Expert** — **Эксперт предметной области** ([Domain-Driven Design: стратегическое проектирование. Часть 1 / Habr](https://habrahabr.ru/post/316438/#:~:text=%D0%94%D0%BB%D1%8F%20%D1%82%D0%BE%D0%B3%D0%BE%20%D1%87%D1%82%D0%BE%D0%B1%D1%8B%20%D1%83%D1%80%D0%B0%D0%B2%D0%BD%D1%8F%D1%82%D1%8C%20%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA%D0%BE%D0%B2,%D0%B8%20%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D1%8B%D0%B9%20%D0%BF%D0%BE%D0%B7%D0%B6%D0%B5%20%D0%BE%D1%82%D1%80%D0%B0%D0%B7%D0%B8%D1%82%D1%81%D1%8F%20%D0%B2))  
A subject matter specialist who possesses deep knowledge of the business domain. Domain experts collaborate closely with the development team to share insights and clarify requirements, ensuring the software’s model and language accurately reflect real-world domain knowledge​

**Context Mapping** — **Карта контекстов** ([Domain-Driven Design: стратегическое проектирование. Часть 1 / Habr](https://habrahabr.ru/post/316438/#:~:text=%D0%9A%D0%B0%D1%80%D1%82%D0%B0%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BA%D1%81%D1%82%D0%BE%D0%B2))  
A technique to identify and define relationships between multiple bounded contexts in a large system. A context map makes explicit how contexts interact or integrate (e.g. partnership, customer-supplier, conformist) and helps visualize the boundaries between subdomains, including mechanisms like anti-corruption layers between them​

**Event Storming** — **Событийный штурм** ([Моделирование микросервисов. Часть 2 / Хабр](https://habr.com/ru/articles/745830/#:~:text=%D0%A1%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9%D0%BD%D1%8B%D0%B9%20%D1%88%D1%82%D1%83%D1%80%D0%BC%20,%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D1%81%D1%81%D0%BE%D0%B2))  
A collaborative workshop format for rapidly exploring a domain by modeling events. Stakeholders from different roles gather to brainstorm domain events (notable happenings in the business), typically using sticky notes on a timeline. This visual process helps everyone understand what is occurring in the business process and discover insights about the domain​

**Anti-Corruption Layer (ACL)** — **Антикоррупционный слой** ([Domain Driven Design: что это такое и как его использовать](https://tproger.ru/articles/domain-driven-design-davajte-ne-budem-uslozhnyat#:~:text=,%D0%BC%D0%B5%D0%BD%D1%8F%D0%B5%D1%82%D1%81%D1%8F%20%D1%82%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE%20%D0%BE%D0%BD%D0%B0%2C%20%D0%B0%20%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0))  
A protective translation layer that isolates one bounded context (or system) from another with a different model. The ACL converts or adapts communications between the two so that one context’s design is not “corrupted” by concepts from the other. This allows systems to integrate without forcing domain changes on either side

**Subdomain** — **Предметная подобласть** A specific section of the overall business domain, representing a distinct area of responsibility or knowledge. DDD categorizes subdomains into three types: **Core** (central to the business’s competitive advantage, where most effort is focused), **Supporting** (assists the core domain but is not fundamental to unique value), and **Generic** (common solutions not unique to the business, often reusable or off-the-shelf)​

