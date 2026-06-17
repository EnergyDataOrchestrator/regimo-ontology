


```mermaid
 classDiagram
    class Contact
    click Contact href "../Contact"
      Contact : affiliation
        
          
    
        
        
        Contact --> "*" Affiliation : affiliation
        click Affiliation href "../Affiliation"
    

        
      Contact : contact_id
        
      Contact : mbox
        
      Contact : name
        
      
```
