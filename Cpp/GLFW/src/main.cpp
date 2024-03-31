#include <GLFW/glfw3.h>

int main(void)
{
	GLFWwindow* window;

	if (!glfwInit()){
		return -1;
	}

	window = glfwCreateWindow(500, 500, "Hello World", NULL, NULL);

	if (!window){
		glfwTerminate();
		return -1;
	}

	while(!glfwWindowShouldClose(window)){
		glClear(GL_COLOR_BUFFER_BIT);

    glBegin(GL_TRIANGLES);
    glVertex2f(-0.1f, -0.1f);
    glVertex2f(0.0f, 0.1f);
    glVertex2f(0.1f, -0.1f);
    glEnd();

		glfwSwapBuffers(window);
		glfwPollEvents();
	}

	glfwTerminate();
	return 0;
}
