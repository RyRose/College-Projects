#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include "exec.h"

void exec(struct command *cmd) {
    int i; int j;
    int input_fd; int output_fd;
    int fds[2];
    int* input_array_fd; int* output_array_fd; int* child_array_pid;
    int pid;

    input_fd = 0; // 0 is default for keyboard. Else is PID of file.
    output_fd = 1; // 1 is default for monitor. Else is PID of file.
    input_array_fd  = (int*) malloc(sizeof(int)*cmd->num_cmds);
    output_array_fd = (int*) malloc(sizeof(int)*cmd->num_cmds);
    child_array_pid = (int*) malloc(sizeof(int)*cmd->num_cmds);

    if (cmd->src_file != NULL) input_fd = open(cmd->src_file, O_RDONLY);
    if (cmd->dst_file != NULL) {
	output_fd = open(cmd->dst_file, O_WRONLY);
    } else {
	output_array_fd[cmd->num_cmds - 1] = 1;
    }
    output_array_fd[0] = output_fd;	
    input_array_fd[0] = input_fd;
    

    for( i = 1; i < cmd->num_cmds; i++ ) {
	pipe(fds);
	input_array_fd[ i ] = fds[0];
	output_array_fd[i - 1] = fds[1];
    }

    

    for( i = 0; i < cmd->num_cmds; i++) {
	pid = fork();
	if (pid == 0) {
	    
	    if( input_array_fd[i] != 0 ) {
		close(0);
		dup(input_array_fd[i]);
	    }

	    if( output_array_fd[i] != 1 ) {
		close(1);
		dup(output_array_fd[i]);
	    }

	    for ( j = 0; j < cmd->num_cmds; j++) {
		if ( input_array_fd[j] != 0 ) {
		    close(input_array_fd[j]);
		}
		if ( output_array_fd[j] != 1 ) {
		    close(output_array_fd[j]);
		}
	    }

	    free(input_array_fd);
	    free(output_array_fd);
	    free(child_array_pid);

	    execvp(cmd->cmd_args[i][0], cmd->cmd_args[i]);
	    write(1, "Command not found\n", 19);
	    exit(-1);
	} else {
	    child_array_pid[i] = pid;
        }
    }

    for ( j = 0; j < cmd->num_cmds; j++) {
	if ( input_array_fd[j] != 0 ) {
	    close(input_array_fd[j]);
	}
	if ( output_array_fd[j] != 1 ) {
	    close(output_array_fd[j]);
	}
    }

    for( i = 0; i < cmd->num_cmds; i++ ) {
	waitpid(child_array_pid[i], NULL, 0);
    }


    free( input_array_fd );
    free( output_array_fd );
    free( child_array_pid );
}

