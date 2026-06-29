<?php 

  include "RDMO_linkML.class.php";
  
  
  if (count($argv) < 2)
	  die("usage: ./{$argv[0]} <rdmo-output-file.json>");
 
  $r = new RDMO_linkML($argv[1]);

  print join("\n", $r->get_linkml_kv_pairs());


