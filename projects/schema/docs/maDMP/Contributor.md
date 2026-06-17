


```mermaid
 classDiagram
    class Contributor
    click Contributor href "../Contributor"
      Contributor : affiliation
        
          
    
        
        
        Contributor --> "*" Affiliation : affiliation
        click Affiliation href "../Affiliation"
    

        
      Contributor : contributor_id
        
      Contributor : mbox
        
      Contributor : name
        
      Contributor : role
        
          
    
        
        
        Contributor --> "1" ContributorRoles : role
        click ContributorRoles href "../ContributorRoles"
    

        
      
```
