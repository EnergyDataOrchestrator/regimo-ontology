<?php 

  if (count($argv) < 2)
	  die("usage: ./{$argv[0]} <rdmo-output-file.json>");

  include "RDMO_linkML.class.php";
 
  $r = new RDMO_linkML($argv[1]);

  print $r->generate_rdmo_linkml_definition();

