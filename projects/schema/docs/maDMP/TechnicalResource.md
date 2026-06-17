


```mermaid
 classDiagram
    class TechnicalResource
    click TechnicalResource href "../TechnicalResource"
      TechnicalResource : description
        
      TechnicalResource : name
        
      TechnicalResource : technical_resource_id
        
          
    
        
        
        TechnicalResource --> "*" TechnicalResourceID : technical_resource_id
        click TechnicalResourceID href "../TechnicalResourceID"
    

        
      
```
