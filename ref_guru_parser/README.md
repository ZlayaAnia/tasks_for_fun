# **PatternParser**

## **About**

PatternParser is a simple class for parsing information about object-oriented programming patterns.

There are two methods:
 - PatternParser.list_pattern(): Allows you to get the names of all programming patterns from the refactoring.guru website as a list.
- PatternParser.list_pattern(obj): Allows you to get a description of a pattern by its name

## **Usage**

Import and initialization
```
>>> from main import PatternParser
>>> pat = PatternParser()
```
Get a list of pattern's names:
```
>>> pat.list_pattern()
['Factory Method', 'Abstract Factory', 'Builder', 'Prototype', 'Singleton', 
'Adapter', 'Bridge', 'Composite', 'Decorator', 'Facade', 
'Flyweight', 'Proxy', 'Chain of Responsibility', 'Command',
'Iterator', 'Mediator', 'Memento', 'Observer', 'State', 'Strategy'
'Template Method', 'Visitor']
```
Get information about pattern:
```
>>> pat.pattern_info("proxy")
'Proxy is a structural design pattern that lets you provide a substitute or placeholder for another object. 
A proxy controls access to the original object,
allowing you to perform something either before or after the request gets through to the original object.'

>>> pat.pattern_info("pro")
This pattern is not on the site, try with other names. 
Available names can be obtained with PatternParser.list_pattern()

```
