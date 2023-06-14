#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - This is a function that prints bytes information.
 * @p: Python Object
 * Return: NULL
 */

void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, k, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (k = 0; k < limit; k++)
		if (string[i] >= 0)
			printf(" %02x", string[k]);
		else
			printf(" %02x", 256 + string[k]);

	printf("\n");
}

/**
 * print_python_list - This function prints list information.
 *
 * @p: Python Object
 * Return: no return
 */

void print_python_list(PyObject *p)
{
	long int size, k;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (k = 0; k < size; k++)
	{
		obj = ((PyListObject *)p)->ob_item[k];
		printf("Element %ld: %s\n", k, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);

}
