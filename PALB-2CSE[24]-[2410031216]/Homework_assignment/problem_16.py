def common_element(arr1,arr2,arr3):
    i,j,k=0
    n1,n2,n3=len(arr1),len(arr2),len(arr3)
    result=[]
    while i<n1 and j<n2 and k<3:
        if arr1[i]==arr2[j]==arr3[k]:
            result.append(arr1[i])
            val=arr1[i]
            while i<n1 and arr1[i]==val:i=i+1
            while i<n1 and arr1[i]==val:j=j+1
            while i<n1 and arr1[i]==val:k=k+1
        elif arr1[i]<arr2[j]:
            curr= arr1[i]
            while j<n1 and arr1[i] ==curr:i=i+1
        elif arr1[i]<arr2[j]:
            curr= arr1[i]
            while j<n1 and arr1[i] ==curr:i=i+1
        elif arr1[i]<arr2[j]:
            curr= arr1[i]
            while j<n1 and arr1[i] ==curr:i=i+1

