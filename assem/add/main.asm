global _start

section .text


_start:
	;FIRST MESSAGE
	MOV rax, 1
	MOV rdi, 1
	MOV rsi, prompt
	MOV rdx, promptlen	
	SYSCALL

	;FIRST INPUT
	MOV rax, 0
	MOV rdi, 0
	MOV rsi, n1
	MOV rdx, 2	
	SYSCALL
	
	;SECOND MESSAGE
	MOV rax, 1
	MOV rdi, 1
	MOV rsi, prompt
	MOV rdx, promptlen	
	SYSCALL
	
	;SECOND INPUT
	MOV rax, 0
	MOV rdi, 0
	MOV rsi, n2
	MOV rdx, 2	
	SYSCALL

	;MOVING n1, n2 to rbx, rcx
	MOV rbx, [n1]
	SUB rbx, '0'
	MOV rcx, [n2]
	SUB rcx, '0'
	
	;ADDING rcx in rbx
	ADD rbx, rcx
	ADD rbx, '0'
	MOV [n3], rbx		;n3 = rbx


	;STDOUT N3
	MOV rax, 1
	MOV rdi, 1
	MOV rsi, n3
	MOV rdx, 1
	SYSCALL

	;EXIT
	MOV rax, 60
	MOV rdi, 0
	SYSCALL
	
section .data
	prompt : DB "Enter a number : ", 0x0
	promptlen : EQU $ - prompt

section .bss
	n1 resb 0
	n2 resb 0
	n3 resb 0 	
