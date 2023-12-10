global _start

section .text


_start:
	MOV rax, 1
	MOV rdi, 1
	MOV rsi, prompt
	MOV rdx, plen	
	SYSCALL

	MOV rax, 0
	MOV rdi, 0
	MOV rsi, name
	MOV rdx, 100
	SYSCALL

	MOV rax, 1
	MOV rdi, 1
	MOV rsi, name
	MOV rdx, 100	
	SYSCALL

	MOV rax, 60
	MOV rdi, 0
	SYSCALL
section .data
	name : TIMES 100 DB 0
	prompt : DB "ENTER NAME : ", 0x0
	plen : EQU $ - prompt

