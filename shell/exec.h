#ifndef _EXEC_H_
#define _EXEC_H_

/* structure representing the component parts of a user's line */
struct command {
    char *src_file;   /* pointer to input file, or NULL if keyboard */
    char *dst_file;   /* pointer to output file, or NULL if display */
    int   num_cmds;   /* number of commands in user input */
    char ***cmd_args; /* array of pointers to arrays of commands' args */
};

void exec(struct command *cmd);

#endif /* _EXEC_H_ */
