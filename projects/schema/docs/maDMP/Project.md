


```mermaid
 classDiagram
    class Project
    click Project href "../Project"
      Project : description
        
      Project : end
        
      Project : funding
        
          
    
        
        
        Project --> "0..1" Fundings : funding
        click Fundings href "../Fundings"
    

        
      Project : project_id
        
          
    
        
        
        Project --> "*" ProjectID : project_id
        click ProjectID href "../ProjectID"
    

        
      Project : start
        
      Project : title
        
      
```
