


```mermaid
 classDiagram
    class Creator
    click Creator href "../Creator"
      Creator : affiliation
        
          
    
        
        
        Creator --> "*" Affiliation : affiliation
        click Affiliation href "../Affiliation"
    

        
      Creator : creator_id
        
      Creator : mbox
        
      Creator : name
        
      
```
