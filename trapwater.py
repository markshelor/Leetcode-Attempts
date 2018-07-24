class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #Just checking some input characteristics
        print(len(height))
        print('\n')
        
        #Loop variable declaration
        x=0
        j=0
        filler=0
        trap=0
        i=0
        k=0
        while i <= (len(height))-1: 
            
            print('We start with i=', i)
            
            #Ensure this isn't the last item
            if i==len(height)-1:
                print('but this is the last item...')
                break
            #Ensure we have something in front of us
            #if i+1==len(height)-1:
            #    print('theres nothing in front')
            #    break
            else:
                #Look to the right for something as tall or taller than h[i]
                print('something in front')
                j=0
                while x<1:
                    #print('x is',x)
                    #j acts as a loop variable and holds the index, which is transferred to x.
                    j=j+1
                    print('j=',j)

                    
                    
                    #If you arrive at the last entry in the array
                    if i+j==len(height)-1:
                        print('i + j =',i+j)
                        
                        #check the last entry
                        if height[i+j]>=height[i]:
                            x=i+j
                            j=0
                            print('Pillar index is', x)
                            break
                        
                        
                        
                        
                        #check for any ascending scales x distance away, h[i]>h[i+1]<h[i+2]...
                        j=0
                        while (i+j)<len(height)-1:
                            j=j+1
                            print('inner j is',j)
                            
                            #If there aren't, bail
                            if i+j==len(height):
                                print('things got weird')
                                i=i+1
                                print('so now i is ',i)
                                break
                            
                            #If there are more than one, k captures the index of the taller one.    
                            if k!=0 and height[k]>height[i+j]:
                                print('k is already: ',k)
                                break
                                
                            if height[i+j]>height[i+j-1]:
                                k=i+j
                                print('k: ',k)
                        if k==0:
                            print('intensifies')
                            continue

                        #find a left bound
                        print('k is ',k)
                        for d in range (i+1,k):
                            if height[d]>=height[k]:
                                if d>0:
                                    i=d
                                    print(i)
                                    continue
                            
                        for n in range (i+1,k):
                            filler=filler+height[n]
                            print('special filler is',filler)
                        
                        
                        print('final filler is ',filler)
                        print('pretrap i is ',i)
                        trap=trap+height[k]*(k-i-1)-filler
                        print('special trap is',trap)
                        filler=0        
                        if k>0:
                            i=k
                        print('also, i is now ',i)
                        print('\n')
                        k=0
                        x=-1
                        j=0
                        break
                    
                    
                    if i+j>=len(height)-1:
                        print('how did we get here')
                        i=i+1
                        break
                    
                    #check for something as tall or taller than h[i]
                    if height[i+j]>=height[i]:
                        x=i+j
                        j=0
                        print('Pillar index is', x)
                        break 
            
                    
                #Once we have the index of the closest pillar that is 'as high' as h[i]
                #Volume in this 2d space is base*height-fillers
                for n in range (i+1,x):
                    filler=filler+height[n]
                    print('filler is',filler)
                    
                if x==0:
                        print('The temptation to use goto intensifies')
                        j=0
                        i=i+1
                        print('i increased to: ',i)
                        continue
                if x==-1:
                    print('so that happened')
                    continue
                
                trap=trap+(height[i]*(x-i-1))-filler
                print('amount trapped is now',trap)
                filler=0
            #Once you have the volume trapped, move to this new pillar and look to its right.
        
            if x==0:
                print('help')
                x=i+1
            i=x
            x=0
            print('i should be',i)
            print('\n')
        return(trap)        
        
