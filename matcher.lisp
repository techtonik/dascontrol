; -*- mode: lisp; coding: utf-8 -*-

;; (ql:quickload "cl-match")
;; (ql:quickload "split-sequence")
;; (ql:quickload "vas-string-metrics")
;; (use-package :split-sequence)

(defparameter *rules-trivial* (make-hash-table :test #'equal))

(defun define-trivial-rule (string action)
  (setf (gethash string *rules-trivial*) action))

(defun match-trivial (text)
  (gethash text *rules-trivial*))

(defun match-form (text)
  ;; (let* (words (split-sequence #\Space text))
  nil)
    
    
(defun match-keyword (text)
  nil)

(defun match (text)
  (or (match-trivial text)
      (match-form text)
      (match-keyword text)
      ""))

(define-trivial-rule "сделай громче"  "sound.volume.inc")
(define-trivial-rule "сделай тише"    "sound.volume.dec")
(define-trivial-rule "запусти музыку" "music.start")

(with-open-file (infile "sample.txt" :direction :input :if-does-not-exist nil)
  (with-open-file (outfile "action.txt" :direction :output)
    (format outfile (match (read-line infile)))))

