<?php
require_once 'classes/CreateDocx.php';

$docx = new CreateDocx();
$docx->transformDocument('document.pdf', 'output.docx', 'msword');