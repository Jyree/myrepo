#include <iostream>
#include <vector>
#include <stdio.h>
#include <cstring>

using namespace std;

int heap_sz = 0;
vector<int> heap;

void siftUp(int i)
{
	while(i > 1 && heap[i] < heap[i / 2])
	{
		register int t = heap[i];
		heap[i] = heap[i / 2];
		heap[i / 2] = t;
		i = i / 2;
	}
}

void siftDown(int i)
{
	while(2 * i <= heap_sz)
	{
		int j = i;
		if(heap[2 * i] < heap[j])
			j = 2 * i;
		if(2 * i + 1 <= heap_sz && heap[2 * i + 1] < heap[j])
			j = 2 * i + 1;
		if(i == j)
			break;
		register int t = heap[j];
		heap[j] = heap[i];
		heap[i] = t;
		i = j;
	}
}

void add(int x)
{
	heap_sz++;
	heap[heap_sz] = x;
	siftUp(heap_sz);
}

void extract(void)
{
	//cout << heap_sz << endl;
	if(heap_sz == 0)
	{
		cout << "CANNOT" << endl;
		return;
	} else
	{
		cout << heap[1] << " ";
		heap[1] = heap[heap_sz];
		heap_sz--;
		siftDown(1);
		return;
	}
}

void clear(void)
{
	heap_sz = 0;
}

void init(void)
{
	heap_sz = 0;
	heap.resize(200100);
}

void init(int x)
{
	heap_sz = 0;
	heap.resize(x+1);
}

int main()
{
	//freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	register int k = 0;
	register int t;
	cin >> k;
	init(k+1);
	for(int i = 1; i <= k; i++)
	{
		cin >> t;
		add(t);
	}
	for(int i = 1; i <= k; i++)
	{
		extract();
	}
	return 0;
}