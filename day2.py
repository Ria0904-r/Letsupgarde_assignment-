{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    1\n",
      "   22\n",
      "  333\n",
      " 4444\n",
      "55555\n"
     ]
    }
   ],
   "source": [
    "for i in range(1,6):\n",
    "    for j in range(5,i,-1):\n",
    "        print(\" \",end=\"\")\n",
    "    for z in range(0,i):\n",
    "        print(i,end=\"\")\n",
    "    print()    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "list1 = [12, 3, 55, 6, 144]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[12, 6, 144]\n"
     ]
    }
   ],
   "source": [
    "x=[num for num in list1 if num % 2==0]\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "list2=[2, 10, 9, 37]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 10]\n"
     ]
    }
   ],
   "source": [
    "x=[num for num in list2 if num % 2==0]\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
