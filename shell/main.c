#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "exec.h"

#define LINE_LEN 1024

/* error codes for parseCommand */
#define EMPTY_COMMAND -1
#define BAD_IN_REDIRECT -2
#define BAD_OUT_REDIRECT -3

void grow(void **base, int *len, int cell);
int parseCommand(struct command *cmd, char *line);
void freeCommand(struct command *cmd);

int main() {
    char line[LINE_LEN];
    struct command cmd;
    char *fgets_ret;
    int i;

    while (1) {
        printf("mysh%% ");
        fgets_ret = fgets(line, LINE_LEN - 1, stdin);
        if (fgets_ret == NULL) break;
        i = strlen(line);
        while (i > 0 && line[i - 1] < 32) i--;
        line[i] = '\0';

        i = parseCommand(&cmd, line);
        switch (i) {
        case 0:
            exec(&cmd);
            freeCommand(&cmd);
            break;
        case EMPTY_COMMAND:
            printf("EMPTY_COMMAND\n");
            break;
        case BAD_IN_REDIRECT:
            printf("BAD_IN_REDIRECT\n");
            break;
        case BAD_OUT_REDIRECT:
            printf("BAD_OUT_REDIRECT\n");
            break;
        default:
            printf("unrecognized error code %d\n", i);
        }
    }
    return 0;
}

/* parseCommand
 *  Parses a line typed by the user in the shell into its
 *  component parts, returning an error code.
 *
 * Parameters:
 *  cmd - points to structure where to place information about line.
 *  line - a pointer to the line typed by the user.
 *
 * Returns:
 *  0 if the line is valid, a nonzero error code (as
 *  listed in parse.h) if invalid.
 */
int parseCommand(struct command *cmd, char *line) {
    /* The below implementation is written to be hard to follow.
     * Writing this function has been an assignment in the past;
     * and so that it can be assigned later, I don't want to post
     * an ideal solution.  Do not read or copy this implementation! */

    int k;int m;int n;int r;char**a;int*l;cmd->src_file=NULL;cmd->
    dst_file=NULL;r=0;a=(char**)malloc(sizeof(char*)*4);m=0;l=(int*)
    malloc(sizeof(int)*4);n=1;l[0]=0;k=0;for(;*line;line++){switch(*
    line){case'<':*line='\0';if(n>1||cmd->src_file!=NULL||k==1){r=
    BAD_IN_REDIRECT;goto done;}if(k==2){r=BAD_OUT_REDIRECT;goto done
    ;}k=1;break;case'>':*line='\0';if(cmd->dst_file!=NULL||k==2){r=
    BAD_OUT_REDIRECT;goto done;}if(k==1){r=BAD_IN_REDIRECT;goto done;
    }k=2;break;case' ':case'\t':*line='\0';if((k&12)==4)k=(20-k)&0xF;
    break;case'|':*line='\0';if(cmd->dst_file!=NULL||k==2){r=
    BAD_OUT_REDIRECT;goto done;}if(k==1){r=BAD_IN_REDIRECT;goto done;
    }grow((void**)&a,&m,sizeof(char*));a[m-1]=NULL;grow((void**)&l,&n
    ,sizeof(int*));l[n-1]=m;k=0;break;default:switch(k){case 0:grow((
    void**)&a,&m,sizeof(char*));a[m-1]=line;break;case 1:cmd->src_file
    =line;break;case 2:cmd->dst_file=line;break;case 14:r=
    BAD_OUT_REDIRECT;goto done;case 15:r=BAD_IN_REDIRECT;goto done;}
    if((k&12)==0)k|=4;}}done:grow((void**)&a,&m,sizeof(char*));a[m-1]
    =NULL;cmd->num_cmds=n;cmd->cmd_args=(char***)malloc(sizeof(char
    **)*n);for(m=0;m<n;m++){cmd->cmd_args[m]=a+l[m];if(a[l[m]]==NULL
    )r=EMPTY_COMMAND;}free(l);if(!r)r=k==1?BAD_IN_REDIRECT:k==2?
    BAD_OUT_REDIRECT:0;if(r)freeCommand(cmd);return r;
}

void freeCommand(struct command *cmd) {
    free(cmd->cmd_args[0]);free(cmd->cmd_args);
}

void grow(void **base, int *len, int cell) {
    void *newb;if(*len>=4&&(*len&-*len)==*len){newb=malloc(2*cell**len
    );memcpy(newb,*base,cell**len);free(*base);*base=newb;}(*len)++;
}
