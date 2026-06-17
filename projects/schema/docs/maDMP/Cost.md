


```mermaid
 classDiagram
    class Cost
    click Cost href "../Cost"
      Cost : currency_code
        
          
    
        
        
        Cost --> "0..1" CurrencyCode : currency_code
        click CurrencyCode href "../CurrencyCode"
    

        
      Cost : description
        
      Cost : title
        
      Cost : value
        
      
```
