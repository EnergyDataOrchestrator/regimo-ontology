<?php

class RDMO_linkML {

	function __construct($rdmo_file, $header_file='templates/rdmo_header.linkML') {
		$this->rdmo_file = $rdmo_file;
		$this->header_file = $header_file;
	}


	static function transform_question2property($val) {
		$tmp = preg_replace('/\?.*/', '', strtolower($val)); 
		$tmp = preg_replace('/ /', '_', $tmp); 
		return  preg_replace('/[^_A-Za-z0-9\n]/', '', $tmp); 
	}

	function rdmo_header() {
		return file_get_contents($this->header_file);
	}

	function get_linkml_attributes() {
		$json = file_get_contents($this->rdmo_file);
		$json = json_decode($json);
		$attributes = [];
		foreach ($json as $item) {
			# print_r($item);
			# print "Q:".$item->question."\nA:".
			$attributes[] = self::transform_question2property($item->question);
		}
		return $attributes;
	}

	function generate_rdmo_linkml_definition() {
		$header = $this->rdmo_header();
		$atts = $this->get_linkml_attributes();
		$oindent = "      ";
		return $header."      ".
			   join(":\n      ", $atts).":\n";
	}
	
	function get_linkml_kv_pairs() {
		$json = file_get_contents($this->rdmo_file);
		$json = json_decode($json);
		$kv_pair = [];
		foreach ($json as $item) {
			$values =  preg_replace('/"/', '\\"', $item->values);
			$kv_pair[] = self::transform_question2property($item->question).": \"$values\"";
		}
		return $kv_pair;
	}
}

